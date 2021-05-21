import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IPais } from './pais.model';

@Component({
    selector: 'car-pais-detail',
    templateUrl: './pais-detail.component.html'
})
export class PaisDetailComponent implements OnInit {
    pais!: IPais;

    constructor(private activatedRoute: ActivatedRoute) {}

    ngOnInit(): void {
        this.activatedRoute.data.subscribe(({ pais }) => this.pais = pais);
    }
}
