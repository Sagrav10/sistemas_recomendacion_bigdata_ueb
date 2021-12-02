import {NgModule} from '@angular/core';

import {DashboardRoutingModule} from './dashboard-routing.module';

import {SharedModule} from '../shared/shared.module';
import {HomeComponent} from './home/home.component';


@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    SharedModule,
    DashboardRoutingModule,
  ],
})
export class DashboardModule {
}