const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const multer = require("multer");

const upload = multer({
  storage: multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
      cb(null, file.originalname);
    }
  }),
});
const app = express();

app.use(cors());
app.use(morgan("combined"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.post("/upload", upload.array("file[]"), (req, res) => {
  console.log(req.files);

});

app.get('/download',(req, res) => {
   const filePath = "/server/uploads/final_800.png";        // const filePath = "/server/uploads/"; 
   const  fileName = "final_800.png";
   res.download(filePath, fileName);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log("Server running...");
});