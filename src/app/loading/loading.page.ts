import { Component, OnInit } from '@angular/core';
import {NavController,NavParams, } from '@ionic/angular'
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";
import {HttpParams} from "@angular/common/http";
import { HttpClientModule } from '@angular/common/http';

import { FinalPage } from '../final/final.page';
import { HomePage } from '../home/home.page';
import * as _ from 'lodash';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.page.html',
  styleUrls: ['./loading.page.scss'],
})
export class LoadingPage implements OnInit {
  
  constructor(
    private http: HttpClient,
    private router: Router,
    ) { }

  ngOnInit() {
   
  }

  test(){
    alert("ing");
    //로딩 페이지에 들어오면 서버에서 합성 완료 신호를 받으면 다음 페이지로 넘어갑니다
    if(this.http.get('http://localhost:8100/home')){
      this.navigateToFinal();
    }
  }
    
  navigateToFinal(){
   
    console.log("navigateToFinal");
    this.router.navigate(['final']);
  }
  
}
