$(document).ready(function(){
	var uploadButton = $("#upload-button")

	uploadButton.on("click", function(){
		file = $("#file-form").prop("files")[0];
		$.ajax(
			url: "/api/files/" + file.name,
			method: "PUT",
			headers: {"content-type": "image/jpeg"}
			)
	})

})