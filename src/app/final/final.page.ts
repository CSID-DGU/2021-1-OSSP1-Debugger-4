import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";


import { HomePage } from '../home/home.page';
import * as _ from 'lodash';

@Component({
  selector: 'app-final',
  templateUrl: './final.page.html',
  styleUrls: ['./final.page.scss'],
})
export class FinalPage implements OnInit {
  private file:File;

  constructor(
    //private http: HttpClient,
    private router: Router,
  ) { }

  ngOnInit() {
    // Simple GET request with response type <any>
    //this.http.get('http://210.94.194.107:3000/upload"').subscribe(data => {
    //   this.resultFile = data;  }
  }

  navigateToHome(){
    console.log("navigateToHome");
    this.router.navigate(['home']);
  }
  
  receiveFile(PR){

    let formData = new FormData();
    formData.append("file[]", this.file, this.file.name);
    //this.http.post("http://localhost:8100/home", formData).subscribe((response) => {
    //  console.log(response);
    //});
  }
  downLoadImg(){
    
  }
}
