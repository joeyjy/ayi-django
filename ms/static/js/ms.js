/* Project specific Javascript goes here. */
$('.h-t').hover(function(){
	$(this).css('cursor','pointer');
	$(this).next('.tooltip').show();
}, function() {
	$(this).next('.tooltip').hide();
});

$('.popdown').click(function(){
	var ups = $(this).attr("id"); 
	$('#bpop-'+ups).bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
        speed: 450,
        transition: 'slideDown'
    });
});