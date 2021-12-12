var _MS_PER_DAY = 1000 * 60 * 60 * 24;

// a e b sono oggetti Data
function dateDiffInDays(a, b) {
  // Esclude l'ora ed il fuso orario
  var utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
  var utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());

  return Math.floor((utc2 - utc1) / _MS_PER_DAY);
}

function getDateDiffInDays() {
 var YA = document.getElementById("YA").value
 var MA = document.getElementById("MA").value
 var DA = document.getElementById("DA").value
 var YB = document.getElementById("YB").value
 var MB = document.getElementById("MB").value
 var DB = document.getElementById("DB").value

 var date1 = new Date(YA + "/" + MA + "/" + DA);
 var date2 = new Date(YB + "/" + MB + "/" + DB);

 var el = document.getElementById("date_diff")
 el.innerHTML = dateDiffInDays(date1, date2)
}