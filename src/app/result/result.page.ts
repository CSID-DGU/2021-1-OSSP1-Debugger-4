import { Component, OnInit} from '@angular/core';
import {NavController,NavParams, } from '@ionic/angular'
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";
import {HttpParams} from "@angular/common/http";
import { HomePage } from '../home/home.page';


import { HttpClientModule } from '@angular/common/http';
//import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';


@Component({
  selector: 'app-result',
  templateUrl: 'result.page.html',
  styleUrls: ['result.page.scss'],
})
export class ResultPage  implements OnInit {

  constructor(
    private http: HttpClient,
    private router:Router
   ) {}

  resultFile;
  ngOnInit() {      
    // Simple GET request with response type <any>
    //this.http.get('http://210.94.194.107:3000/upload"').subscribe(data => {
    //   this.resultFile = data;  }
  } /*
  navigateToHome(){
    console.log("navigateToHome");
    this.router.navigate(['home']);
  }



  /*
  receiveFile(PR){

    this.fileTransfer.download("http://210.94.194.107:3000/upload")
    return this.http.get("http://210.94.194.107:3000/upload",
    {params:new HttpParams().set('result',PR)});
    
  }
/*
  getResult() : File{
    file = this.receiveFile();
  }
*/
//
 
}

