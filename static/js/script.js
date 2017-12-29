$(document).ready(function(){
	$("#myitems").toggle();

	
	$("#form_buy_product").on('submit',function(event){
		event.preventDefault();
		var numb = $('#number').val();
		var submit_btn = $("#submit_btn");
		var product_id = submit_btn.data("product_id");
		var product_name = submit_btn.data("product_name");
		var product_price = submit_btn.data("product_price")

		data = {};

		data.product_id = product_id;
		
		data.numb = numb;



		
		
		$("#myitems").append("<li>"+ product_name + "," + numb + "," + product_price +
			"<a class='delete-item' href=''>x</a>" +
		 "</li>");

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