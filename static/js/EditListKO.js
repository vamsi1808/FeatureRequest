
ko.validation.init({
    registerExtenders: false,
    messagesOnModified: true,
    insertMessages: true,
    parseInputAttributes: true,
    errorClass: 'errorStyle',
    messageTemplate: null
}, true);

function ReqDetails() {
    var parsedData;
	var feature_id = $('#feature_id').val()
    $.ajax({
        type: 'GET',
        url: '/features/' + feature_id + '/',
        contentType: "application/javascript",
		async:false,
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
	var that = this;
	that.feature_title = ko.observable(parsedData.feature_title)
	that.feature_desc = ko.observable(parsedData.feature_desc);
	that.client_name = ko.observable(parsedData.client_name);
	that.priority = ko.observable(parsedData.client_priority);
	that.target_date = ko.observable(parsedData.target_date);
	that.product_area = ko.observable(parsedData.product_area)
}

function RequisiteDetailsVM() {
    var that = this;
    that.ReqDetails = new ReqDetails();
    
    that.reset = function () {
        window.location.href = "/featurescreen"
    };
};
var _vm = new RequisiteDetailsVM();

$(function () {
    ko.applyBindings(_vm);
});

