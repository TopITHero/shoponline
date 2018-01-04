$(document).ready(function(){
	$("#myitems").toggle();

	
	$("#form_buy_product").on('submit',function(event){
		event.preventDefault();
		var numb = $('#number').val();
		var submit_btn = $("#submit_btn");
		var product_id = submit_btn.data("product_id");
		data = {};

		data.product_id = product_id;
		
		data.numb = numb;

		var  csrf_token = $('#form_buy_product input[name ="csrfmiddlewaretoken"]').val(); 
		
		var url = $("#form_buy_product").attr("action");
		data['csrfmiddlewaretoken'] = csrf_token
		
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache:true,
			success: function(json){
					console.log(json);
					$("#buyproduct").html(json);
			}
		});

		$("li").on("click", ".btn", function(event){
			event.preventDefault();
			console.log("delete")
			var close = $(this).parent();
			$.ajax({
				url: $(this).attr("href"),
				type: 'DELETE',
				data: {
					'delete': true,
				},
				success: function(json) {
					$("#buyproduct").html(json);
					close.fadeOut(1000);
				}
			});
		});	


		
		
		
	});
	$("#buyproduct").click(function(){
        $("#myitems").toggle();

    });

    $(document).on('click', '.delete-item', function(event){
    	event.preventDefault();
    	$(this).closest("li").remove();
    	$("#myitems").toggle();	
    });
});