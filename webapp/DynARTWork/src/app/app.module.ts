import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { UploadImageComponent } from './upload-image/upload-image.component';

import { AngularFireModule } from '@angular/fire';
import { AngularFireStorageModule, BUCKET} from '@angular/fire/storage';
import { AngularFireFunctionsModule, REGION, ORIGIN} from '@angular/fire/functions';

import { environment } from '../environments/environment';
import { AppMaterialModule } from './app-material.module';

@NgModule({
  declarations: [
    AppComponent,
    UploadImageComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireFunctionsModule,
    AppMaterialModule
  ],
  providers: [
    { provide: BUCKET, useValue: environment.firebase.storageBucket}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
