// --- Landing page ---
$(document).ready(function () {
    $(".index-info-section").hide();
    $(".landing-image").hide();
    setTimeout(function () {$(".landing-image").slideDown(1500); }, 1000);
    setTimeout(function () {$(".index-info-section").slideDown(1500); }, 2500);
});
