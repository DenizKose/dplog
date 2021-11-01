$(document).ready(function() {
    setTimeout(getTime,10)
    console.log('start repeat')
    setInterval(
        getTime
        , 1000);
    console.log('1s')
})
function getTime(){
    const datePlace = document.getElementById('date')
    const timePlace = document.getElementById('time')
    const time = new Date(Date.now())
    const month = [];
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";
    const m = month[time.getMonth()]

    datePlace.innerHTML = addZero(time.getDate())+' '+addZero(m)
    timePlace.innerHTML = addZero(time.getHours())+':'+addZero(time.getMinutes())
}

function addZero(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}