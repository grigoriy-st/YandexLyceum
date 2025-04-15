// Создать хранилище сессий пользователей. Время работы каждой сессии (TTL) составляет 2 минуты.
package main

import (
	"sync"
	"time"
)

type Session struct {
	ID        string
	UserID    string
	ExpiresAt time.Time
}

type SessionManager struct {
	sessions map[string]Session
	mutex    sync.RWMutex
}

func NewSessionManager() *SessionManager {
	return &SessionManager{
		sessions: make(map[string]Session),
	}
}

func (sm *SessionManager) StartSession(userID string) string {
	sm.mutex.Lock()
	defer sm.mutex.Unlock()
	sessionID := "random"

	session := Session{
		ID:        sessionID,
		UserID:    userID,
		ExpiresAt: time.Now().Add(2 * time.Minute),
	}

	sm.sessions[sessionID] = session
	return sessionID
}

func (sm *SessionManager) GetSession(sessionID string) (Session, bool) {
	sm.mutex.RLock()
	defer sm.mutex.RUnlock()

	session, exists := sm.sessions[sessionID]

	if !exists || time.Now().After(session.ExpiresAt) {
		return Session{}, false
	}

	return session, true
}
