import { Component, OnInit } from '@angular/core';
//import {NavController,NavParams, } from '@ionic/angular'
import { Router } from '@angular/router';
import { HttpClient } from "@angular/common/http";
//import 'rxjs/add/operator/toPromise';


//import {HttpParams} from "@angular/common/http";
//import { HttpClientModule } from '@angular/common/http';

import { FinalPage } from '../final/final.page';
import * as _ from 'lodash';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.page.html',
  styleUrls: ['./loading.page.scss'],
})
export class LoadingPage implements OnInit {
private result:File;
  
  constructor(
    private http: HttpClient,
    private router: Router,
    ) { }

  ngOnInit() {
  
  }
  navigateToFinal(){
    console.log("navigateToFinal");
    this.router.navigate(['final']);
  }

  go(){
    this.navigateToFinal();
  }

}
