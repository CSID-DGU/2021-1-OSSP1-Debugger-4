const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const multer = require("multer");
var http = require('http');
const app = express();
const util = require('util');
require('util.promisify').shim();

const fs = require('fs');
const readFileAsync = util.promisify(fs.readFile);

const upload = multer({
  storage: multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, '../server/uploads/');
    },
    filename: function (req, file, cb) {
      cb(null, file.originalname);
    }
  }),
});




app.use(cors());
app.use(morgan("combined"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/image",function(req,res){

res.sendFile('/home/plass-sukhyun/2021-1-OSSP1-Debugger-4/preprocess/result.png');

});


app.post("/", upload.array("file[]"), function(req, res)  {
  console.log(req.files);

var {PythonShell} = require('python-shell');
var options = {

  mode: 'text',
  pythonPath: '',
  pythonOptions: ['-u'],
  scriptPath: '',

};
/*
PythonShell.run('../2021-1-OSSP1-Debugger-4/facesynthesis.py', options,  (err, msg) =>{
  if (err) throw err;
  if (msg == "Complete"){
  var imgdata = JSON.parse('../2021-1-OSSP1-Debugger-4/result.json').img;
  console.log(imgdata);
}
  });*/


let pyshell = new PythonShell('../2021-1-OSSP1-Debugger-4/facesynthesis.py', options) // Options 설정 가능


// Python Script로부터 출력된 결과 값 받기(Python Script의 print에서 받아오는 값이 msg임)



pyshell.end((err, code, signal) => {
	if(err) throw err;
    console.log('The exit code was: ' + code);
  	console.log('The exit signal was: ' + signal);
  	console.log('finished');
});




});









const port = process.env.PORT || 3001;

app.listen(port, () =>{
	console.log("Upload Server running on 3000...");
});




