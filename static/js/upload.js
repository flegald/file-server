$(document).ready(function(){

	$( '#upload-form' )
	  .submit( function( e ) {
	    $.ajax( {
	      url: '/api/files/hello',
	      type: 'POST',
	      data: new FormData( this ),
	      headers: {"X-Session": localStorage.getItem("sessionJWT")},
	      processData: false,
	      contentType: false,
	      complete: function(data){
	      	console.log(data);
	      }
	    } );
	    e.preventDefault();
	  } );

})