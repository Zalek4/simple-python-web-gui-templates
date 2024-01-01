//This creates a timer of 3 seconds. The loading screen will play for that duration, and then load the main program.

let count = 3;
const timer = setInterval(function() {
    count--;
    console.log(count);
    if (count === 0) {
    clearInterval(timer);
    console.log("Time's up!");
    switchPage()
    }
}, 1000);

function switchPage() {
    document.location.href = '/home';
}