$(document).ready(function(){

	$( '#view-files' )
	  .click( function( e ) {
	    $.ajax( {
	      url: '/api/view/files',
	      type: 'GET',
	      headers: {"X-Session": localStorage.getItem("sessionJWT")},
	      complete: function(data){
			if (data.status != 200) {
				alert("Error: " + data.status + " " + data.responseText)
			} else {
		      	$.each(data.responseJSON["files"], function(i){
		      		   var li = $('<li/>')
		      		   	.text(data.responseJSON["files"][i])			
				        .appendTo($("#files-list"));
				})
	      	}
	      }
	    } );
	    e.preventDefault();
	  } );

})