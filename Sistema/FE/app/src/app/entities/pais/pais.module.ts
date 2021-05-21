import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CineArPaisCommonsModule } from "./pais.commons.module";
import { paisRoute } from "./pais.route";

const ENTITY_STATES = [...paisRoute]
@NgModule({
    imports: [CineArPaisCommonsModule, RouterModule.forChild(ENTITY_STATES)]
})
export class CineArPaisModule{}