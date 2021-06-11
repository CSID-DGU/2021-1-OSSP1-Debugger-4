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

app.get('/upload/',(req, res) => {
   res.download('uploads/final_800.png', "final_800");
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log("Server running...");
});