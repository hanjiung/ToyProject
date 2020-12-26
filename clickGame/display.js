
// if clicked, execute the function
for(var i = 1; i <= 9; i++) {
    document.getElementById("visual" + i).addEventListener("click", clicking)
}

// When this function is excuted, the number of clickNum variable is increased.
var clickNum = 0;
function clicking()
{
    clickNum += 1;
    document.getElementById('clicks').innerHTML = clickNum;
}

// this function make the random number output.
function blocking() {
    var id = setInterval(function() {
        var b = Math.floor(Math.random() * (9 - 1 + 1)) + 1;
        var a = document.getElementById('visual' + b)
        a.style.display = 'block'
        setTimeout(function() {
            a.style.display = 'None'
        },2000);
    }, 2000);

}

// blocking function executes
blocking();
