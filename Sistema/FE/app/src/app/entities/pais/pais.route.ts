import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { PaisUpdateComponent } from './pais-update.component';
import { IPais, Pais } from './pais.model';
import { PaisService } from './pais.service';
import { PaisDetailComponent } from './pais-detail.component';
import { PaisComponent } from './pais.component';

@Injectable({ providedIn: 'root' })
export class PaisResolve implements Resolve<IPais> {
    constructor(private paisService: PaisService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.paisService.find(id).pipe(map((res: HttpResponse<IPais>) => res.body!))
            : of(new Pais());
    }
}

export const paisRoute: Routes = [
    {
        path: '',
        component: PaisComponent
    },
    {
        path: ':id/view',
        component: PaisDetailComponent,
        resolve: {
            pais: PaisResolve
        },
        data: {
            pageTitle: 'Pais'
        }
    },
    {
        path: ':id/edit',
        component: PaisUpdateComponent,
        resolve: {
            pais: PaisResolve
        },
        data: {
            pageTitle: 'Pais'
        }
    },
    {
        path: 'new',
        component: PaisUpdateComponent,
        resolve: {
            pais: PaisResolve
        },
        data: {
            pageTitle: 'Pais'
        }
    },
];
