import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';

import { AngularFireStorage } from '@angular/fire/storage';

@Component({
  selector: 'app-upload-image',
  templateUrl: './upload-image.component.html',
  styleUrls: ['./upload-image.component.scss']
})
export class UploadImageComponent implements OnInit {
  @Input() placeholder: string;
  @Input() nomeImage: string;
  @Output() urlCreated = new EventEmitter<string>();
  uploadPercent: Observable<number>;
  downloadURL: Observable<string>;
  imageUrl: string = null;
  isLoading: boolean;

  constructor(private storage: AngularFireStorage) { }

  ngOnInit(): void {
  }
  uploadFile(event) {
    this.isLoading = true;
    console.log(event);
    const file = event.target.files[0];
    const filePath = `images/${this.nomeImage}`;
    const fileRef = this.storage.ref(filePath);
    const task = this.storage.upload(filePath, file);
    console.log(file);
    // observe percentage changes
    this.uploadPercent = task.percentageChanges();
    // get notified when the download URL is available
    task.snapshotChanges().pipe(
        finalize(() => {
          this.downloadURL = fileRef.getDownloadURL();
          this.downloadURL.subscribe(res => {
              this.imageUrl = res;
              this.urlCreated.emit(res);
              this.isLoading = false;
            });
        })
     )
    .subscribe(data => {
      console.log(fileRef.getDownloadURL());
    });

  }

}
