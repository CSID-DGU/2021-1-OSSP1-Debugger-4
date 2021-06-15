import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { IonicModule } from '@ionic/angular';

import { FinalPageRoutingModule } from './final-routing.module';
import { FinalPage } from './final.page';

import {FileTransfer} from '@ionic-native/file-transfer/ngx';
import {FileChooser} from '@ionic-native/file-chooser/ngx';
import {FilePath} from '@ionic-native/file-path/ngx';
import {File} from '@ionic-native/file/ngx';

import { FileUploadOptions, FileTransferObject } from '@ionic-native/file-transfer/ngx';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FinalPageRoutingModule
  ],
  declarations: [FinalPage],
  providers:[
    FileTransfer,
    FileChooser,
    FilePath,
    File
  ]

})
export class FinalPageModule {}
