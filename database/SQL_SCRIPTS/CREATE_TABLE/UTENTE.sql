-- CREAZIONE UTENTE
CREATE TABLE UTENTE(  
   ID                          INTEGER      PRIMARY KEY AUTO_INCREMENT,  
   NOME_UTENTE                 VARCHAR(64)    NOT NULL,  
   COGNOME_UTENTE              VARCHAR(64)    NOT NULL,
   EMAIL                       VARCHAR(64)    NOT NULL UNIQUE, 
   USERNAME                    VARCHAR(64)    NOT NULL UNIQUE,
   PASSWORD_HASH               VARCHAR(128)   NOT NULL,
   CONFIRMED                   TINYINT(1)     NOT NULL, 
   ULTIMO_ACCESSO              DATE           NOT NULL,
   SESSO_UTENTE                CHAR(20)       NOT NULL, 
   DATA_DI_NASCITA_UTENTE      DATE           NOT NULL,          
   TELEFONO_UTENTE             CHAR(10)       NOT NULL, 
   CITTA_UTENTE                VARCHAR(64)    NOT NULL,
   PROVINCIA_UTENTE            VARCHAR(64)    NOT NULL,
   VIA_UTENTE                  VARCHAR(120)   NOT NULL,
   CAP_UTENTE                  INTEGER        NOT NULL,
   DATA_CREAZIONE_UTENTE       DATE           NOT NULL
)