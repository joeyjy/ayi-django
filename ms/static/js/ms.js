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

(function($) {
    $.extend({
        doGet: function(url, params) {
            document.location = url + '?' + $.param(params);
        },
        doPost: function(url, params) {
            var $form = $("<form method='POST'>").attr("action", url);
            $.each(params, function(name, value) {
                $("<input type='hidden'>")
                    .attr("name", name)
                    .attr("value", value)
                    .appendTo($form);
            });
            $("input[name=csrfmiddlewaretoken]").appendTo($form);
            $form.appendTo("body");
            $form.submit();

        },
        querystringToObject: function(querystring) {
            var obj = {};
            var params = querystring.split("&");
            for (var i = 0; i < params.length; i++) {
                var temp = params[i].split("=");
                if (temp[0]) {
                    if (temp.length < 2) {
                        temp.push("");
                    }
                    obj[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
                }
            }
            return obj;
        },
        urlGet:function() {
            var aQuery = window.location.href.split("?");  //取得Get参数
            var aGET = new Array();
            if(aQuery.length > 1)
            {
                var aBuf = aQuery[1].split("&");
                for(var i=0, iLoop = aBuf.length; i<iLoop; i++)
                {
                    var aTmp = aBuf[i].split("=");  //分离key与Value
                    aGET[aTmp[0]] = aTmp[1];
                }
             }
             return aGET;
        }
    });
})(jQuery);