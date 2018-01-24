jQuery(document).ready(function () {
    jQuery("#list").jqGrid(
        {

			url:'features/',
			contentType: "application/json; charset=utf-8",
            datatype: 'json',
            //Method Type
            mtype: 'GET',
            //Columns Name
            colNames: ['RequisitionId', 'Title', 'Description', 'Client', 'Client Priority', 'Target Date', 'Product Area', 'Action'],
            colModel:[
				{ name: 'id', hidden: true },
                { name: 'feature_title', sorttype: 'string' },
                { name: 'feature_desc', width: 200 },
                { name: 'client_name', sorttype: 'string'},
                { name: 'client_priority', align: 'right', sorttype: 'int'},
                { name: 'target_date', align: 'left', formatter: 'date', formatoptions: { srcformat: "ISO8601Long", newformat: "m/d/Y" } },
                { name: 'product_area'},
                {
                    name: 'act', align:'center', isExported: false, index: 'act', sortable: false, width:100, formatter: actionFormatter, frozen: true
                }	
			],
			loadBeforeSend: function(jqXHR) {
				jqXHR.setRequestHeader("Authorization", 'JWT '+ window.sessionStorage.accessToken);
			},
            pager: jQuery('#pager'),
            //Record per Page By Default
            rowNum: 10,
            //Record Per Page Dropdown
            rowList: [5, 10, 20, 30, 40, 50],
            gridview: true,
            viewrecords: true,
            loadonce: true,
            //Enables or disables the show/hide grid button
            hidegrid: false,
            recordtext: "View {0} - {1} of {2}",
            pgtext: "Page {0} of {1}",
            //AltRows Colour
            altRows: true,
            emptyrecords: 'No Records are Available to Display',
			autowidth: true,
			height:'auto',
            loadComplete: function (data) {
			},
			loadError: function (jqXHR, textStatus, errorThrown) {
				console.log('HTTP status code: ' + jqXHR.status + 'n' +
				'textStatus: ' + textStatus + 'n' +
				'errorThrown: ' + errorThrown);
				console.log('HTTP message body (jqXHR.responseText): ' + 'n' + jqXHR.responseText);
				if(errorThrown=="Unauthorized"){
					window.location.href = "/"
				}
			},
			jsonReader: {
				repeatitems: false,
				id: "Id",
				root: function (obj) { return obj; },
				page: function (obj) { return 1; },
				total: function (obj) { return 1; },
				records: function (obj) { return obj.length; }
			}
        });
        jQuery("#list").jqGrid('navGrid', '#pager',
            { edit: false, add: false, del: false, view: false},
        {},
        {},
        {},
        { multipleSearch: true, multipleGroup: false });

    function actionFormatter(cellvalue, options, rowObject) {
        return "<a href='viewscreen/"+rowObject.id+"/'><i class='fa fa-fw fa-server'></i></a>";
    }
        function utcDateFormatter(cellvalue, options, rowObject) {
            if (cellvalue) {
                return moment(cellvalue).utc().format("MM/DD/YYYY");
            } else {
                return '';
            }
        }
});