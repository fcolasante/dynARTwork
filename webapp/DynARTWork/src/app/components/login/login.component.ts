import { Component, OnInit } from '@angular/core';
import {AngularFireAuth} from '@angular/fire/auth';
import {AuthProvider} from 'ngx-auth-firebaseui';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(public afAuth: AngularFireAuth) { }
  
  providers = AuthProvider;
    
  ngOnInit(): void {
  }
  printUser(event) {
    console.log(event);
  }

  printError(event) {
   console.error(event);
  }

}
