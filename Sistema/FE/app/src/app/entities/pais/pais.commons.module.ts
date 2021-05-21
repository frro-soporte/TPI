import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import { PaisDetailComponent } from "./pais-detail.component";
import { PaisUpdateComponent } from "./pais-update.component";
import { PaisComponent } from "./pais.component";

@NgModule({
    imports: [RouterModule,CascadeSelectModule],
    declarations: [
        PaisComponent,
        PaisDetailComponent,
        PaisUpdateComponent],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})

export class CineArPaisCommonsModule{}