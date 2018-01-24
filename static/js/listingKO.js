function AppViewModel() {
    var self = this;
	var parsedData;
	$.ajax({
        type: 'GET',
        url: 'features/',
        contentType: "application/javascript",
        dataType: "json",
        async:false,
		cache:false,
		beforeSend: function(request) {
					request.setRequestHeader("Authorization", 'JWT '+ window.sessionStorage.accessToken);
		},
        success: function (data) {
            parsedData = data;
        },
        error: function (jq, st, error) {
            if(error=="Unauthorized"){
				window.location.href = "/"
			}
        }
    });
    self.requistions = ko.observableArray(parsedData);
}

ko.applyBindings(new AppViewModel());