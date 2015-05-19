var parameters= document.getElementById("parameters_pie_chart").getContext("2d");

var pieData = [
	{
		value: 0.05,
		color:"#878BB6",
		label: "baryons"
	},
	{
		value: 0.70,
		color: "#4ACAB4",
		label: "dark energy"
	},
	{
		value: 0.25,
		color: "#FF8153",
		label: "dark matter"
	}
];

var pieOptions = {
	segmentShowStroke : false,
	animateScale : true
}

new Chart(parameters).Pie(pieData, pieOptions);
