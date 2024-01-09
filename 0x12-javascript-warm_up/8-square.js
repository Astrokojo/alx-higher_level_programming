#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)){
	console.log("Missing size");
} else {
	for (let outer = 0; outer < size; outer++){
	let row = "";
		for (let inner = 0; inner < size; inner++) 
			row += "X";
			console.log(row);
		
	}
};
