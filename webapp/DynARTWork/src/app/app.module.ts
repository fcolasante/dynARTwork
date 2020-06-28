import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing/app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { UploadImageComponent } from './upload-image/upload-image.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


import { AngularFireModule } from '@angular/fire';
import { AngularFireStorageModule, BUCKET} from '@angular/fire/storage';
import { AngularFireAuthModule } from '@angular/fire/auth';
import { AngularFireFunctionsModule, REGION, ORIGIN} from '@angular/fire/functions';
import { NgxAuthFirebaseUIModule } from 'ngx-auth-firebaseui';




import { environment } from '../environments/environment';
import { AppMaterialModule } from './app-material.module';
import { AboutComponent } from './components/about/about.component';
import { ContactComponent } from './components/contact/contact.component';
import { HomeComponent } from './home/home.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';
import { LoginComponent } from './components/login/login.component';
import { TeamComponent } from './components/team/team.component';


@NgModule({
  declarations: [
    AppComponent,
    UploadImageComponent,
    HomeComponent,
    ToolbarComponent,
    ContactComponent,
    AboutComponent,
    LoginComponent,
    TeamComponent
 ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxAuthFirebaseUIModule.forRoot({
      apiKey: "AIzaSyDzj9WdlpAO2gSI2zKMAk6dmB6c17TusQQ",
      authDomain: "dynartwork-277815.firebaseapp.com",
      databaseURL: "https://dynartwork-277815.firebaseio.com",
      projectId: "dynartwork-277815",
      storageBucket: "dynartwork-277815.appspot.com",
      messagingSenderId: "1026699295478"
    },
    () => 'your_app_name_factory',
   {
     enableFirestoreSync: true, // enable/disable autosync users with firestore
     toastMessageOnAuthSuccess: false, // whether to open/show a snackbar message on auth success - default : true
     toastMessageOnAuthError: false, // whether to open/show a snackbar message on auth error - default : true
     authGuardFallbackURL: '/loggedout', // url for unauthenticated users - to use in combination with canActivate feature on a route
     authGuardLoggedInURL: '/loggedin', // url for authenticated users - to use in combination with canActivate feature on a route
     passwordMaxLength: 60, // `min/max` input parameters in components should be within this range.
     passwordMinLength: 8, // Password length min/max in forms independently of each componenet min/max.
     // Same as password but for the name
     nameMaxLength: 50,
     nameMinLength: 2,
     // If set, sign-in/up form is not available until email has been verified.
     // Plus protected routes are still protected even though user is connected.
     guardProtectedRoutesUntilEmailIsVerified: true,
     enableEmailVerification: true, // default: true
   }),
  //  NgxAuthFirebaseUIModule.forRoot(firebasekey, "DynArtWork",
  //   {
  //     authGuardFallbackURL: 'examples/logged-out',
  //     authGuardLoggedInURL: 'examples/logged-in',
  //   }),
    BrowserAnimationsModule,
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireAuthModule,
    AngularFireFunctionsModule,
    AppMaterialModule,
    FormsModule,
    ReactiveFormsModule,

  ],
  providers: [
    { provide: BUCKET, useValue: environment.firebase.storageBucket}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
