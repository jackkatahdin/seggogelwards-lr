var button_f = $("#forward_button");
button_f.click(function() {
    console.log(button_f.text());
    if (button_f.text() === "Forward") {
        $.ajax({
            url: "/forward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_f.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_f.text("Forward");
            }
        })
    }
});
var button_b = $("#backward_button");
button_b.click(function() {
    console.log(button_b.text());
    if (button_b.text() === "Backward") {
        $.ajax({
            url: "/backward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_b.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_b.text("Backward");
            }
        })
    }
});

button_r.click(function() {
    if (button_r.text() === "Right") {
	button_r.text("Stop");
    } else {
	button_r.text("Right");
    }
});


button_r.click(function() {
    if (button_r.text() === "Left") {
	button_r.text("Stop");
    } else {
	button_r.text("Left");
    }
});
