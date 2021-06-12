import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";
import { LoadingPage } from '../loading/loading.page';
import { FinalPage } from '../final/final.page';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage {
private file: File;
private file2: File;
  constructor(
    private http: HttpClient,
    private router: Router)
  {

  }

  
  navigateToLoading(){
    //this.submitForm();
    this.router.navigate(['loading']);
    //this.router.navigate(['loading']);

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
    this.http.post("http://210.94.194.107:3000/upload",
     formData).subscribe((response) => {
      console.log("보내기 성공");
    });
    this.navigateToLoading();
  }

}


