import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";

import { LoadingPage } from '../loading/loading.page';
import { ResultPage } from '../result/result.page';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],

})

export class HomePage {
private file: File;
private file2: File;
  constructor(private http: HttpClient,private router: Router)
  {}

  navigateToLoading(){
    //this.submitForm();
    console.log("navigateToLoading");
    this.router.navigate(['loading']);

  }
  
  onFileChange(fileChangeEvent) {
    this.file = fileChangeEvent.target.files[0];
  }
  onFile2Change(fileChangeEvent){
    this.file2 = fileChangeEvent.target.files[0];
  }

  async submitForm() {
    let formData = new FormData();
    formData.append("file[]", this.file, this.file.name);
    formData.append("file[]",this.file2,this.file2.name);
    this.http.post("http://localhost:8100/home", formData).subscribe((response) => {
      console.log(response);
    });
    //http://210.94.194.107:3000/upload
  }
    

}


