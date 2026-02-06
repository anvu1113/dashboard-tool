from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time
import json
from app.core.logging import request_logger

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Process request
        try:
            response = await call_next(request)
            
            process_time = (time.time() - start_time) * 1000
            formatted_process_time = int(process_time)
            
            log_data = {
                "type": "request",
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "latency_ms": formatted_process_time
            }
            
            # Log to file
            request_logger.info(json.dumps(log_data))
            
            return response
            
        except Exception as e:
            process_time = (time.time() - start_time) * 1000
            log_data = {
                "type": "request_error",
                "method": request.method,
                "path": request.url.path,
                "status": 500,
                "latency_ms": int(process_time),
                "error": str(e)
            }
            request_logger.error(json.dumps(log_data))
            raise e
