import { NgModule } from '@angular/core';
import { RouterModule, Routes} from '@angular/router'
import { HomeComponent } from '../home/home.component';
import { ContactComponent } from '../components/contact/contact.component';
import { AboutComponent } from '../components/about/about.component';
import { LoginComponent } from '../components/login/login.component';
import { UploadImageComponent } from '../upload-image/upload-image.component';
import {LoggedInGuard} from 'ngx-auth-firebaseui';
import { TeamComponent } from '../components/team/team.component';

const appRoutes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'contact', component: ContactComponent},
  {path: 'about', component: AboutComponent},
  {path: 'login', component: LoginComponent},
  {path: 'newDynArtWork', component: UploadImageComponent},
  {path: 'team', component: TeamComponent},
  {
    path: 'secured',
    loadChildren: 'app/secured/secured.module#SecuredModule',
    canActivate: [LoggedInGuard]
  }

]


@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes)
  ], 
  exports:[
    RouterModule
  ]
})
export class AppRoutingModule { }
