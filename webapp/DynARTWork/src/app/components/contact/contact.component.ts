import { Component, OnInit,ViewChild } from '@angular/core';
import {FormControl, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import {ErrorStateMatcher} from '@angular/material/core';
 import { MatDialog } from '@angular/material/dialog';


/** Error when invalid control is dirty, touched, or submitted. */
export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {
  @ViewChild('contactForm') public contactForm: any;
  contactReasons: Array<any> = [
    { value: 'help-needed', viewValue: 'Help Needed' },
    { value: 'general-question', viewValue: 'General Question' },
    { value: 'complaint', viewValue: 'Complaint' }
  ];
  //material.io
  emailFormControl = new FormControl('', [
    Validators.required,
    Validators.email,
  ]);

  matcher = new MyErrorStateMatcher();

  
  ngOnInit(): void {
  }
  onContactFormSubmit(formData) {
    this.contactForm.submitting = true;
    setTimeout(() => {
      this.contactForm.submitting = false;
      this.contactForm.reset();
      if (formData.optIn) {
        alert(`Your ${formData.subject} message has been sent and you\'ve been subscribed to the mailing list!`);
      } else {
        alert(`Your ${formData.subject} message has been sent!`)
      }
    }, 1500);
  }

  // onContactFormClear() {
  //   let dialogRef = this.dialog.open(ConfirmClearDialogComponent);
  //   dialogRef.afterClosed().subscribe(result => {
  //     if (result && result.shouldClear) {
  //       this.contactForm.reset();
  //     }
  //   };
}
