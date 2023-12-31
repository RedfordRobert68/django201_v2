// console.log("Hello world!")
// console.log("This is frontend")

$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;

            if (document.cookie && document.cookie !== ''){
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1){
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        if(!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    }
})

/************************************************
Modal Toggle
************************************************/
$(document).on("click", ".js-toggle-modal", function(e) {
    e.preventDefault()
    $(".js-modal").toggleClass("hidden");
})

$(document).on("click", ".close-btn-js", function(e) {
    e.preventDefault()
    $('.overlay, .js-modal').addClass("hidden");
})

$(document).on("click", ".js-submit", function(e) {
    e.preventDefault()
    console.log("I was clicked!")
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)

    if(!text.length){ //If there is no post, do nothing when "Create Post" button has been selected
        return false
    }
    

    $btn.prop("disabled", true).text("Posting!")

    $.ajax({
        type: 'POST',
        url: $(".js-post-text").data("post-url"),
        data: {
            text: text
        },
        success: (dataHTML) => {
            $(".js-modal").addClass("hidden");
            $("#posts-container").prepend(dataHTML);
            $btn.prop("disabled", true).text("New Post");
            $(".js-post-text").val("") //Remove text in the field after "Create Post" button has been selected
            location.reload(true);
           
        },
        error: (error)=> {
            console.warn(error)
            $btn.prop("disabled", false).text("Error");
        }
    });
});

/********************************************** 
Follow Button
**********************************************/
$(document).on("click", ".js-follow", function(e) {
    e.preventDefault();
    
    const action = $(this).attr("data-action")
    $.ajax({
        type: 'Post',
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success: (data) => {
            $(".js-follow-text").text(data.wording)
            location.reload(true);

            if(action == "follow") {
                $(this).attr("data-action", "unfollow")
            } else {
                $(this).attr("data-action", "follow")
            }
        },
        error: (error)=> {
            console.warn(error)
        }
    });
})

/********************************************
Toggle full comment
********************************************/

$(document).ready(function(){
    var x = document.getElementById("rm");
    $('.rm-js').click(function(){
        $(this).toggleClass('rm-js');
        $(this).text($(this).text() == 'Read less' ? 'Read more' : 'Read less');
        $(this).parent().find('.rm1').toggleClass('block');
        $(this).parent().find('.rm2').toggleClass('hidden');
    }); 
});


/*************************************************** 
Remove duplicate friends by class names
****************************************************/
$(document).ready(function(){
    var elem = {};
    $('div#friend').each(function() {
        var txt = $(this).attr('class');
        if (elem[txt])
            $(this).remove();
        else
            elem[txt] = true;
    });
}); 


/*****************************************************
Menu Toggle
******************************************************/
$(document).ready(function(){
    $('#menu-toggle').on("click", function(){
        $('#navigation, .overlay, .hamburger, .closeBtn, header').toggleClass('hidden');
        $('#posts-container').toggleClass('fixed');
    });

    $('.new-post-js').on("click", function(){
        $('#navigation, .overlay, .closeBtn').addClass('hidden');
        $('.overlay_newPost').toggleClass("hidden");
    });

    $('.close-btn-js').on("click", function() {
        $('header, .overlay_newPost, .hamburger').toggleClass("hidden");
        $('#posts-container').toggleClass('fixed');
    })
});










    