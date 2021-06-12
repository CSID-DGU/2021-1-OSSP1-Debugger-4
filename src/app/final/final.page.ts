import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HomePage } from '../home/home.page';
import { HttpClient } from '@angular/common/http';
import { FileTransferObject } from '@ionic-native/file-transfer/ngx';
import {FileTransfer} from '@ionic-native/file-transfer/ngx';

//import * as _ from 'lodash';
//import { FileTransfer } from '@ionic-native/file-transfer/ngx';

@Component({
  selector: 'app-final',
  templateUrl: './final.page.html',
  styleUrls: ['./final.page.scss'],
})

export class FinalPage implements OnInit {
  fileTransfer: FileTransferObject = this.transfer.create();
  file;
  private http: HttpClient;

  constructor(
    private transfer: FileTransfer,
    private router : Router,
  ) { }

 
  ngOnInit() { 
    /*this.http.get('http://210.94.194.107:3000/')///final_800.png
    .subscribe({ next: data => { 
      const url = this.http.get("http://210.94.194.107:3000/upload").subscribe(
        (response) => {console.log(response); });
      this.transfer.download(url, "result.png").then((entry) => {
        console.log('download complete: ' + entry.toURL());  // I always enter here.
      }, (error) => {
        // handle error
        console.log("error!"); 
      });
    }
    });*/
  }


  navigateToHome(){
    console.log("navigateToHome");
    this.router.navigate(['home']);
  }
  
}
