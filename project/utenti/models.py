import hashlib
from datetime import datetime
import uuid
from flask import session, current_app
from flask_login import UserMixin, AnonymousUserMixin
from flask_login._compat import text_type
from itsdangerous import Serializer
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import exc
from wtforms import SubmitField
from werkzeug.security import generate_password_hash, check_password_hash

from project import db, login_manager
from project.Database.dbMysqlAlchemy import db_session, metadata


# CLASSE UTENTE
class Utente(UserMixin, db.Model):
    query = db_session.query_property()
    __tablename__ = 'Utente'
    id_utente = db.Column(db.Integer, primary_key=True)
    nome_utente = db.Column(db.String(64), nullable=False)
    cognome_utente = db.Column(db.String(64), nullable=False)

    username_utente = db.Column(db.String(64), unique=True, index=True)
    email_utente = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    ultimo_accesso = db.Column(db.DateTime(), default=datetime.utcnow)

    sesso_utente = db.Column(db.String(1), nullable=False)
    data_di_nascita_utente = db.Column(db.DateTime, nullable=False)
    telefono_utente = db.Column(db.String(20), nullable=False)
    citta_utente = db.Column(db.String(64), nullable=False)
    provincia_utente = db.Column(db.String(64), nullable=False)
    via_utente = db.Column(db.String(120), nullable=False)
    cap_utente = db.Column(db.Integer, nullable=False)
    data_creazione_utente = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Per conferma mail
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    # Per conferma mail
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
            print(data)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    # Per conferma mail (generazione token)
    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    # Per conferma mail
    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = Utente.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    # Per conferma mail
    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps(
            {'change_email': self.id, 'new_email': new_email}).decode('utf-8')

    # Per cambio mail
    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = self.gravatar_hash()
        db.session.add(self)
        return True

    # Ruoli
    def can(self, perm):
        return self.ruolo is not None and self.ruolo.has_permission(perm)

    '''
    def is_administrator(self):
        return self.can(Permission.ADMIN)
    '''

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    # Avatar
    def gravatar_hash(self):
        return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        url = 'https://secure.gravatar.com/avatar'
        hash = self.avatar_hash or self.gravatar_hash()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    '''
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(
            followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None

    @property
    def followed_posts(self):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id)\
            .filter(Follow.follower_id == self.id)


    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'member_since': self.member_since,
            'last_seen': self.last_seen
            'posts_url': url_for('api.get_user_posts', id=self.id),
            'followed_posts_url': url_for('api.get_user_followed_posts',
                                          id=self.id),
            'post_count': self.posts.count()
        }
        return json_user
    '''

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return Utente.query.get(data['id'])

    def __repr__(self):
        return '<Utente %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return Utente.query.get(int(user_id))
