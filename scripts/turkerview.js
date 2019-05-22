var allValues = {positives:[], negatives:[]};

function extractComments() {
	var positives = document.querySelectorAll('.row > div.col-sm-10 > div > div:nth-child(4) > .text-default');	
	var negatives = document.querySelectorAll('.row > div.col-sm-10 > div > div:nth-child(5) > .text-default');	
	for (var positive of positives) {
		allValues.positives.push(positive.innerText);
	}
	for (var negative of negatives) {
		allValues.negatives.push(negative.innerText);
	}
}
function downloadFile(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
}
function downloadComments() {
    downloadFile(JSON.stringify(allValues), 'data.json', 'text/plain');
}
function printRecords() {
	console.log(allValues.positives.length);
}
function printComments() {
	console.log(JSON.stringify(allValues));
}

extractComments();
printRecords();
downloadComments();
