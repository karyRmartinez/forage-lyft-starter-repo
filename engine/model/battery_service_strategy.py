from service_strategy import ServiceStrategy

class BatteryServiceStrategy(ServiceStrategy):
    def needs_service(self) -> bool:
       
         return self.years_since_last_service() >= 3
