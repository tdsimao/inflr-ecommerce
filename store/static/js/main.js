$(document).ready(function(){
    $(".atom-sidebar-notifications").on("click", function(){
        $("body").addClass("influencers-open");
    })

    $(".atom-influencers-close").on("click", function(){
        $("body").removeClass("influencers-open");
    })
});
