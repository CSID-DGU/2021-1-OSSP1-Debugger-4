import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";
import { LoadingPage } from '../loading/loading.page';
import { timeout,} from 'rxjs/operators';

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

  onFileChange(fileChangeEvent) {
    this.file = fileChangeEvent.target.files[0];
  }
  onFile2Change(fileChangeEvent){
    this.file2 = fileChangeEvent.target.files[0];
  }

    async getData(data)
    {
      //Server를 Local에서 실행 시, http://210.94.194.107:3001/를 http://localhost:3001/ 로 변경.

      await this.http.post("http://210.94.194.107:3001/",data).pipe(timeout(100000000)).toPromise();
      window.location.href = 'http://localhost:8100/final';
    };

    async submitForm()
    {
      this.router.navigate(['/loading']);
      let formData = new FormData();
      formData.append("file[]", this.file, "images.jpg");
      formData.append("file[]",this.file2,"video.mp4");
      await this.getData(formData);
    }

}


