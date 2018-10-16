function init(){
    init_main_canvas();
    init_log_canvas();
    init_util_canvas();


}


function init_main_canvas(){
    let main_canvas = document.getElementById('main_canvas');

    // check whether the user's browser supports canvas or not
    if (main_canvas.getContext) {
        let ctx = main_canvas.getContext('2d');

        ctx.fillStyle = 'black';
        ctx.fillRect(0, 0, main_canvas.width, main_canvas.height);
        let img = new Image();
        img.onload = function(){
            ctx.drawImage(img, 0, 0, main_canvas.width, main_canvas.height);
        };
        //img.src = './_DSC0424.jpg';
    }
    else {
        // if not display an error message
        alert("This browser does not support the canvas element.");
    }
}

function init_log_canvas(){
    let log_canvas = document.getElementById('log_canvas');
    let ctx = log_canvas.getContext('2d');
    ctx.fillStyle = 'green';
    //ctx.fillRect(0, 0, 300, 320);
    ctx.fillRect(0, 0, log_canvas.width, log_canvas.height);

}

function draw_util_tools(){
    let util_canvas = document.getElementById('util_canvas');
    // TODO: add rect click areas and add event listeners
}


function init_util_canvas(){
    let util_canvas = document.getElementById('util_canvas');
    let ctx = util_canvas.getContext('2d');
    ctx.fillStyle = 'yellow';
    ctx.fillRect(0, 0, util_canvas.width, util_canvas.height);
    draw_util_tools();
}


window.onload = init;
