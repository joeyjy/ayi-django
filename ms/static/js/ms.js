/* Project specific Javascript goes here. */
$('.h-t').hover(function(){
	$(this).css('cursor','pointer');
	$(this).next('.tooltip').show();
}, function() {
	$(this).next('.tooltip').hide();
});

$('.lm').click(function(){
	var ups = $(this).attr("id"); 
	$('#bpop-'+ups).bPopup();
});