import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { IonicModule } from '@ionic/angular';

import { LoadingPageRoutingModule } from './loading-routing.module';
import { LoadingPage } from './loading.page';

import {FileTransfer} from
'@ionic-native/file-transfer/ngx';
import {FileChooser} from '@ionic-native/file-chooser/ngx';
import {FilePath} from '@ionic-native/file-path/ngx';
import {File} from '@ionic-native/file/ngx';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    LoadingPageRoutingModule,
    HttpClientModule
  ],
  declarations: [LoadingPage],
  providers:[
    FileTransfer,
    FileChooser,
    FilePath,
    File
  ]
})
export class LoadingPageModule {}
