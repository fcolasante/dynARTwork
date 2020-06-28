import { Component, OnInit } from '@angular/core';
import {NgxAuthFirebaseUIConfig} from 'ngx-auth-firebaseui'
import {AngularFireAuth} from '@angular/fire/auth';
import {User} from 'firebase';
import {Observable} from 'rxjs';
import {MatDialog} from '@angular/material/dialog';
import {UserComponent} from 'ngx-auth-firebaseui';

export interface LinkMenuItem {
  text: string;
  icon?: string;
  callback?: Function;
}

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent implements OnInit {

  user: User;
  user$: Observable<User | null>;
  displayNameInitials: string | null;

  constructor(public afa: AngularFireAuth,
              public dialog: MatDialog) {
  }

  ngOnInit() {
    this.user$ = this.afa.user;
    this.user$.subscribe((user: User) => {
      this.user = user;
      this.displayNameInitials = user ? this.getDisplayNameInitials(user.displayName) : null;
    });
  }

  getDisplayNameInitials(displayName: string | null): string | null {
    if (!displayName) {
      return null;
    }
    const initialsRegExp: RegExpMatchArray = displayName.match(/\b\w/g) || [];
    const initials = ((initialsRegExp.shift() || '') + (initialsRegExp.pop() || '')).toUpperCase();
    return initials;
  }

  openProfile() {
    this.dialog.open(UserComponent);
  }
}
