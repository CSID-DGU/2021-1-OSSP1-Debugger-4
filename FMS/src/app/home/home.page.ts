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

    this.router.navigate(['loading']);
  }

  navigateToFinal(){

      this.router.navigate(['final']);
    }

  onFileChange(fileChangeEvent) {
    this.file = fileChangeEvent.target.files[0];
  }
  onFile2Change(fileChangeEvent){
    this.file2 = fileChangeEvent.target.files[0];
  }



/*this.http.post("http://210.94.194.107:3001/",
                      data).toPromise().subscribe((response) => {

                     });*/
        async getData(data){
        await this.http.post("http://210.94.194.107:3001/",data).toPromise().then()
        //this.router.navigate(['/final']);
        window.location.href = 'http://localhost:8100/final';
        };

    async submitForm() {
    this.router.navigate(['/loading']);

    let formData = new FormData();
    formData.append("file[]", this.file, "images.jpg");
    formData.append("file[]",this.file2,"video.mp4");
    await this.getData(formData);




     }

}


